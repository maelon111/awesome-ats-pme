#!/usr/bin/env python3
"""Temps de tri des CV selon la méthode — modèle reproductible (awesome-ats-pme).

Hypothèses par défaut (estimations, pas des mesures) : 2 min pour enregistrer à la main
une candidature reçue par e-mail, 3 min pour lire un CV en détail, 30 s pour parcourir
un CV moins bien noté quand un score ordonne la pile. Remplacez-les par les vôtres :

    python3 calcul_tri.py --cv 200 --postes 6 --lus 40 --cout-horaire 45
"""
import argparse


def heures_tri(n_cv, saisie_auto, lus_en_detail=None, saisie_min=2.0, lecture_min=3.0, survol_min=0.5):
    """Heures pour trier n_cv. lus_en_detail=None : chaque CV est lu en entier."""
    saisie = 0 if saisie_auto else n_cv * saisie_min
    if lus_en_detail is None:
        lecture = n_cv * lecture_min
    else:
        k = min(lus_en_detail, n_cv)
        lecture = k * lecture_min + (n_cv - k) * survol_min
    return (saisie + lecture) / 60


def hm(h):
    m = round(h * 60)
    return f"{m // 60} h {m % 60:02d}"


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--cv", type=int, default=200, help="CV reçus par poste (200)")
    p.add_argument("--postes", type=int, default=1, help="postes ouverts par an (1)")
    p.add_argument("--lus", type=int, default=40, help="CV lus en détail quand un score ordonne la pile (40)")
    p.add_argument("--saisie", type=float, default=2.0, help="minutes de saisie par CV reçu par e-mail (2)")
    p.add_argument("--lecture", type=float, default=3.0, help="minutes de lecture détaillée (3)")
    p.add_argument("--survol", type=float, default=0.5, help="minutes pour parcourir un CV (0,5)")
    p.add_argument("--cout-horaire", type=float, default=0, help="coût chargé d'une heure, en € (optionnel)")
    p.add_argument("--abonnement", type=float, default=708, help="coût annuel de l'outil avec IA, en € HT (708 = HRSpeeder Platinum mensuel)")
    a = p.parse_args()

    kw = dict(saisie_min=a.saisie, lecture_min=a.lecture, survol_min=a.survol)
    methodes = {
        "Boîte mail + tableur": heures_tri(a.cv, False, None, **kw),
        "ATS sans IA": heures_tri(a.cv, True, None, **kw),
        "ATS avec analyse IA (lecture ordonnée)": heures_tri(a.cv, True, a.lus, **kw),
    }
    print(f"{a.cv} CV par poste, {a.postes} poste(s) par an\n")
    print(f"{'Méthode':42} {'par poste':>10} {'par an':>10}")
    for nom, h in methodes.items():
        print(f"{nom:42} {hm(h):>10} {hm(h * a.postes):>10}")
    gain = (methodes["Boîte mail + tableur"] - methodes["ATS avec analyse IA (lecture ordonnée)"]) * a.postes
    print(f"\nHeures rendues par an : {hm(gain)} (≈ {gain / 7.6:.1f} journées de 7,6 h)")
    if gain and a.abonnement:
        print(f"Coût de l'heure rendue avec un abonnement de {a.abonnement:.2f} € : {a.abonnement / gain:.2f} €")
    if a.cout_horaire:
        print(f"Valeur du temps rendu à {a.cout_horaire:.0f} €/h : {gain * a.cout_horaire:,.0f} €".replace(",", " "))


if __name__ == "__main__":
    main()
