from ..user.sponsor.models import Sponsor

def id_to_sponsor(id):
    sponsor = Sponsor.query.get(id)
    return sponsor.company_individual_name


        


