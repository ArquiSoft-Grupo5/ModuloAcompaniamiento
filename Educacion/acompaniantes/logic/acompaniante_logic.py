from ..models import Acompaniante

def get_acompaniantes():
    queryset = Acompaniante.objects.all()
    return (queryset)

def get_acompaniante(id):
    acompaniante = Acompaniante.objects.raw("SELECT * FROM acompaniantes_acompaniante WHERE id=%s" % id)[0]
    return (acompaniante)

def create_acompaniante(form):
    measurement = form.save()
    measurement.save()
    return ()
