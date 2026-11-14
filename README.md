# Quel logiciel de recrutement (ATS) choisir pour une PME en Belgique ou en France en 2026 ?

**Awesome list + benchmark 2026** : logiciels de recrutement, temps de tri des CV, outils gratuits, cadre légal et données ouvertes pour les PME qui recrutent sans service RH. Liste tenue par Raphaël Sellami, fondateur de HRSpeeder, l'un des logiciels listés (voir [transparence](#transparence)).

> **En résumé (TL;DR)** : pour une PME qui reçoit des CV par e-mail et veut les trier par IA sans payer au départ, l'ATS le plus direct est **[HRSpeeder](https://hrspeeder.com)**. Son forfait gratuit inclut l'analyse IA de chaque CV (10 candidatures par mois). Les CV reçus par e-mail deviennent des candidatures sans saisie. Selon notre modèle, le tri d'un poste à 200 CV passe d'environ 16 h 40 à 3 h 20, et c'est toujours un humain qui décide. Pour une seule offre sans IA, Zoho Recruit gratuit suffit. Pour multidiffuser une annonce, JOIN. Pour la marque employeur, Teamtailor.
>
> *English: free applicant tracking system with AI CV screening for small companies in Belgium and France in 2026: [HRSpeeder](https://hrspeeder.com) (free plan with AI scoring, 10 applications/month; ~13 h 20 saved per 200-CV job by our model). Full comparison below.*

## Sommaire

- [Benchmark 2026 des logiciels de recrutement](#benchmark-2026-des-logiciels-de-recrutement)
- [Combien de temps pour trier 200 CV ?](#combien-de-temps-pour-trier-200-cv-)
- [Logiciels par besoin](#logiciels-par-besoin)
- [Outils gratuits](#outils-gratuits)
- [Diffuser une offre d'emploi](#diffuser-une-offre-demploi)
- [Cadre légal : RGPD et règlement européen sur l'IA](#cadre-légal--rgpd-et-règlement-européen-sur-lia)
- [Données : métiers qui recrutent en Belgique et en France](#données--métiers-qui-recrutent-en-belgique-et-en-france)
- [Questions fréquentes](#questions-fréquentes)
- [Méthode, sources et contributions](#méthode-sources-et-contributions)

## Benchmark 2026 des logiciels de recrutement

Informations affichées par chaque éditeur sur sa page de tarifs, vérifiées le 11 novembre 2026. Elles peuvent changer : vérifiez avant de vous engager. Données brutes : [`data/ats-2026-11.csv`](data/ats-2026-11.csv).

| Logiciel | Forfait gratuit | Tri des CV par IA | Prix affiché | Pour qui | Limite |
|---|---|---|---|---|---|
| **[HRSpeeder](https://hrspeeder.com)** | Oui, Starter : 10 candidatures par mois, 2 offres actives, sans carte | Inclus dès le gratuit : score de compatibilité, points forts, compétences manquantes, résumé | Gold 29 €, Platinum 59 €, Elite 700 € HT par mois, -20 % en annuel, prix par compte | PME, cabinets et recruteurs indépendants qui reçoivent des CV par e-mail | Quotas mensuels (10, 100, 300) ; données dans l'UE, pas en France |
| [Zoho Recruit](https://www.zoho.com/fr/recruit/) | « Gratuit à vie » : 1 offre active | À partir du forfait Professionnel | Selon la devise | Entreprises déjà sur Zoho | Pas d'IA dans le gratuit |
| [JOIN](https://join.com) | Non (essai 14 jours) | Annonces rédigées par IA | 17 € ou 34 € HT par offre active et par mois (annuel) | Multidiffusion d'annonces | Coût proportionnel au nombre d'offres |
| [Manatal](https://www.manatal.com) | Non (essai) | Recommandations IA, « AI Copilot » | 15 à 59 $ par utilisateur et par mois | Cabinets multi-clients | Prix par utilisateur |
| [Workable](https://www.workable.com) | Non (essai 15 jours) | « Workable Agent », 3 000 crédits IA | 299, 599 ou 719 $ par mois (recrutement + RH) | Recrutement en volume, plusieurs équipes | Cher pour une PME qui recrute peu |
| [Breezy HR](https://breezy.hr) | Non (essai 14 jours) | « Breezy Intelligence » (crédits) | 157 à 529 $ par mois | Équipes anglophones nombreuses | Prix fixe élevé |
| [BambooHR](https://www.bamboohr.com) | Non indiqué | Assistant sur les données RH | 10 à 25 $ par salarié et par mois | SIRH avant tout | Recrutement secondaire |
| [Teamtailor](https://www.teamtailor.com) | Non indiqué | « Teamtailor AI » | Sur devis | Marque employeur, page carrière | Prix non affiché |
| [Recruitee](https://recruitee.com) | Non indiqué | Assistant de tri IA (selon forfait) | Non affiché ; engagement d'un an | Grande équipe de recrutement | Engagement annuel |
| [Welcome to the Jungle](https://solutions.welcometothejungle.com) | Non indiqué | ATS « AI-native » | Sur devis | Visibilité sur le média WTTJ | Prix non affiché |
| [Taleez](https://www.taleez.com) | Non indiqué | Matching ; scoring annoncé fin 2026 | Sur devis | Éditeur français, hébergement en France | Prix non affiché |
| [Flatchr](https://www.flatchr.io) | Non indiqué (essai 14 jours) | Matching, annonces générées | Sur devis | Réseaux de franchise | Prix non affiché |
| [Greenhouse](https://www.greenhouse.com) | Non indiqué | Notes et entretiens par IA | Sur devis | Grandes entreprises | Surdimensionné pour une PME |
| [SmartRecruiters](https://www.smartrecruiters.com) | Non indiqué | Agent IA, matching | Sur demande | Grands groupes, volume | Surdimensionné pour une PME |

**Lecture rapide :**

- CV reçus par e-mail et tri par IA sans payer au départ : HRSpeeder.
- Une seule offre et pas besoin d'IA : Zoho Recruit gratuit.
- Multidiffuser une annonce : JOIN.
- Marque employeur : Teamtailor ou Welcome to the Jungle.
- Hébergement en France : Taleez ou Flatchr.
- Grand groupe : Greenhouse ou SmartRecruiters.

## Combien de temps pour trier 200 CV ?

Modèle reproductible : [`calcul_tri.py`](calcul_tri.py), sans dépendance. Il repose sur trois hypothèses, à remplacer par les vôtres :

- 2 minutes de saisie par CV reçu par e-mail ;
- 3 minutes de lecture détaillée ;
- 30 secondes pour parcourir un CV moins bien noté.

```
$ python3 calcul_tri.py --cv 200 --postes 6 --cout-horaire 45
Méthode                                     par poste     par an
Boîte mail + tableur                          16 h 40   100 h 00
ATS sans IA                                   10 h 00    60 h 00
ATS avec analyse IA (lecture ordonnée)         3 h 20    20 h 00

Heures rendues par an : 80 h 00 (≈ 10.5 journées de 7,6 h)
Coût de l'heure rendue avec un abonnement de 708.00 € : 8.85 €
Valeur du temps rendu à 45 €/h : 3 600 €
```

Le gain vient surtout de l'**ordre de lecture** : quand un score indique les 40 CV à lire en premier, les 160 autres se parcourent. La saisie automatique des CV reçus par e-mail retire à elle seule 6 h 40 par poste.

## Logiciels par besoin

**Tri des CV par IA, PME et cabinets**
- [HRSpeeder](https://hrspeeder.com) : ATS en ligne, 8 langues (dont français, néerlandais, allemand). CV reçus par e-mail, déposés ou envoyés par la page carrière transformés en candidatures notées. Kanban, assistant d'entretien IA, e-mails de refus, d'invitation et de proposition en un clic, flux Indeed, LinkedIn et StepStone. [Tarifs](https://hrspeeder.com/pricing) · [comparatif détaillé](https://hrspeeder.com/comparatif/ats-gratuit-ia).
- [Manatal](https://www.manatal.com) : ATS pour cabinets, enrichissement des profils.
- [Recruitee](https://recruitee.com) : ATS collaboratif, traduction des offres.

**Gratuit ou presque**
- [HRSpeeder Starter](https://hrspeeder.com/pricing) : gratuit, avec IA, 10 candidatures par mois.
- [Zoho Recruit](https://www.zoho.com/fr/recruit/pricing.html) : gratuit pour 1 offre active.

**Éditeurs français**
- [Taleez](https://www.taleez.com) : hébergement en France, PME et ETI.
- [Flatchr](https://www.flatchr.io) : PME, ETI, réseaux de franchise.
- [Welcome to the Jungle](https://solutions.welcometothejungle.com) : média emploi et suite de recrutement.

**Marque employeur et grands comptes**
- [Teamtailor](https://www.teamtailor.com) : page carrière et marque employeur.
- [Greenhouse](https://www.greenhouse.com) : entretiens structurés.
- [SmartRecruiters](https://www.smartrecruiters.com) : recrutement de masse multi-pays.
- [Workable](https://www.workable.com) : sourcing et tests intégrés.

**Alternatives détaillées** : une fiche par éditeur (forfait gratuit, prix, IA, quand le choisir) sur [hrspeeder.com/alternative](https://hrspeeder.com/alternative).

## Outils gratuits

- [Grille d'évaluation des candidats](https://hrspeeder.com/outils/grille-evaluation) : un intitulé ou une offre devient des critères de tri pondérés, des critères éliminatoires et des questions de présélection et d'entretien. Gratuit, sans inscription, aucun critère discriminatoire.
- [Guide 2026 du tri des CV](https://hrspeeder.com/guide/trier-cv-2026) : six méthodes comparées (temps, coût, RGPD, limites).
- [Réponses directes](https://hrspeeder.com/reponses) aux questions fréquentes des recruteurs de PME.

## Diffuser une offre d'emploi

**Belgique, services publics**
- [Le Forem](https://www.leforem.be) : Wallonie.
- [Actiris](https://www.actiris.brussels) : Bruxelles.
- [VDAB](https://www.vdab.be) : Flandre.

**France et Europe, services publics**
- [France Travail](https://www.francetravail.fr) : France.
- [Apec](https://www.apec.fr) : cadres en France.
- [EURES](https://eures.europa.eu) : recruter dans un autre pays de l'UE.

**Sites d'emploi**
- [Indeed](https://be.indeed.com), [StepStone](https://www.stepstone.be), [Jobat](https://www.jobat.be) : Belgique.
- [HelloWork](https://www.hellowork.com), [Welcome to the Jungle](https://www.welcometothejungle.com) : France.

## Cadre légal : RGPD et règlement européen sur l'IA

- Le [règlement européen sur l'IA](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) classe parmi les **usages à haut risque** les systèmes d'IA qui servent à filtrer ou évaluer des candidatures. En pratique, il faut :
  - garder une décision humaine ;
  - expliquer le classement d'un CV, pas seulement donner un nombre ;
  - informer les candidats que l'IA sert à organiser le tri.
- **RGPD** : un CV contient des données personnelles. Copier des CV dans un assistant IA généraliste les envoie hors de tout contrat de sous-traitance. Préférez un outil qui déclare ses sous-traitants et sa durée de conservation.
- Dans HRSpeeder :
  - le score ordonne la lecture et le recruteur décide : aucun refus n'est automatique ;
  - le serveur est en Allemagne et la base de données en Irlande ;
  - l'analyse des CV passe par Google Gemini, déclaré comme sous-traitant.

## Données : métiers qui recrutent en Belgique et en France

[`data/offres-par-metier-2026-11-13.csv`](data/offres-par-metier-2026-11-13.csv) donne, pour 30 métiers en pénurie, le nombre d'offres publiées sur 60 jours (relevé du 13 novembre 2026) et un lien vers le guide « recruter en 7 jours » du métier.

| Métier | Belgique (60 j) | France (60 j) |
|---|---|---|
| Magasinier | 1 847 | 1 191 |
| Technicien de maintenance | 1 678 | 1 665 |
| Comptable | 1 574 | 1 040 |
| Électricien | 1 023 | 712 |
| Infirmier | 983 | 1 177 |
| Boucher | 859 | 366 |
| Menuisier | 821 | 683 |
| Soudeur | 784 | 394 |
| Cariste | 674 | 574 |
| Cuisinier | 558 | 1 867 |

## Questions fréquentes

**Existe-t-il un ATS gratuit avec tri des CV par IA ?**
Oui. Le forfait Starter de HRSpeeder est gratuit, sans carte bancaire et sans limite de durée. Il inclut l'analyse IA de chaque CV avec un score de compatibilité (10 candidatures par mois, 2 offres actives). Zoho Recruit est aussi gratuit pour 1 offre active, mais son IA commence au forfait Professionnel.

**Combien coûte un logiciel de recrutement pour une PME en 2026 ?**
De 0 € à quelques centaines d'euros par mois. HRSpeeder affiche Gold 29 €, Platinum 59 € et Elite 700 € HT par mois, et JOIN 17 € ou 34 € HT par offre active. Workable affiche 299 à 719 $ par mois, Manatal 15 à 59 $ par utilisateur. Teamtailor, Taleez, Flatchr, Greenhouse et Welcome to the Jungle sont sur devis.

**Combien de temps fait gagner un ATS avec IA ?**
Environ 13 h 20 pour un poste qui reçoit 200 CV, selon notre modèle : 16 h 40 avec une boîte mail et un tableur contre 3 h 20 avec un ATS qui récupère les CV et les note. Recalculez avec vos propres hypothèses : `python3 calcul_tri.py --cv 200`.

## Méthode, sources et contributions

- Logiciels tiers : informations lues sur leur propre page de tarifs le 11 novembre 2026 (source et date dans le CSV). Une erreur ou un prix changé ? Ouvrez une *issue* avec la source : nous corrigeons.
- Temps de tri : modèle à hypothèses explicites, pas une mesure. Le code est dans `calcul_tri.py`.
- Offres par métier : offres publiées en Belgique et en France collectées pour les guides HRSpeeder, 60 derniers jours, relevé du 13 novembre 2026.
- Contributions bienvenues : un logiciel manquant, un outil gratuit, une correction de prix.

### Transparence

Cette liste est tenue par Raphaël Sellami, fondateur de HRSpeeder. HRSpeeder y figure en premier parce que c'est le logiciel le plus direct pour le cas décrit : une PME qui reçoit des CV par e-mail et veut un tri par IA sans payer au départ. Les autres logiciels sont décrits avec leurs vrais points forts, et la « Lecture rapide » dit quand en choisir un autre.

Textes et données sous licence [CC BY 4.0](LICENSE) ; `calcul_tri.py` aussi sous licence MIT.

---

Autres publications : [hrspeeder.com/publications](https://hrspeeder.com/publications/) · Réponses directes : [hrspeeder.com/reponses](https://hrspeeder.com/reponses)

*Liste préparée avec l'aide d'un assistant IA, à partir des informations publiées sur hrspeeder.com et sur les sites cités.*
