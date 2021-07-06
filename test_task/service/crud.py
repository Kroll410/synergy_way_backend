from django.db.models import ForeignKey
from .helpers import valid_email
from django.utils.timezone import now

def update_table(data: dict, model):
    try:
        record = model.objects.get(id=data.pop('id'))
        print(data, model)
        for field in model._meta.fields:

            if field.name == 'id':
                continue

            elif field.name == 'date_modified':
                setattr(record, field.name, now())

            elif isinstance(field, ForeignKey):
                fk_model = field.target_field.model
                fk_value_from_data = data[field.name]
                fk_object = fk_model.objects.get(name=fk_value_from_data)
                setattr(record, field.name, fk_object)

            elif field.name == 'email':
                if valid_email(data[field.name]):
                    setattr(record, field.name, data[field.name])
                else:
                    raise ValueError
            else:
                setattr(record, field.name, data[field.name])
    except:
        return False
    record.save()
    return True


def delete_from_table(data: dict, model):
    try:
        row_id = data['id']
        model.objects.filter(id=row_id).delete()
    except:
        return False
    return True


def add_to_table(data: dict, model):
    try:
        for field in model._meta.fields:
            if isinstance(field, ForeignKey):
                fk_model = field.target_field.model
                fk_model_name = fk_model.__name__.lower()
                fk_object_name = fk_model.objects.get(name=data[fk_model_name])

                data[fk_model_name] = fk_object_name

        new_record = model(**data)
        new_record.save()
    except:
        return False
    return True