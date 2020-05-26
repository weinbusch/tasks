from wtforms.fields import SelectField

class ModelSelectField(SelectField):

    def __init__(self, query=None, empty=False, empty_label="----", **kwargs):
        
        choices = [(obj.id, str(obj)) for obj in query]
        
        if empty:
            choices.append((None, empty_label))
        
        kwargs["choices"] = choices
        
        def _coerce(value):
            if value:
                return int(value)
            return None
            
        kwargs["coerce"] = _coerce
      
        super().__init__(*args, **kwargs)
        
