# Programació i Algorismia 1 -- Grau en Intel·ligència Artificial

**Jordi Delgado i José Luis Balcázar**

## Pràctica: Treball en equip, novembre de 2024

Aquesta pràctica consisteix a completar la programació d'un "tauler abstracte" que permeti jugar al [3-en-ratlla](https://ca.wikipedia.org/wiki/Tres_en_ratlla), i possiblement alguna variant.

Inicialment només es programarà un tauler on juguen usuaris humans i es mantindrà l'estil funcional que fem servir fins ara, amb declaracions `nonlocal` per assolir l'efecte dit de clausura (closure).

---

## Calendari

Cal que entregueu la pràctica no més tard del dia **13 de gener de 2025**. L'entrega ha de consistir en el codi (tots els fitxers Python que us donem, possiblement modificats per vosaltres, més l'`abs_board.py` complet) i un informe en format lliure, on s'expliqui com heu arribat a la conclusió que el codi que entregueu és una solució correcta al problema plantejat.

---

## Descripció del joc

A les nostres variants del conegut joc, cada partida té dues fases:
1. **Primera fase:** els jugadors col·loquen les seves "pedres" al tauler.
2. **Segona fase:** les jugades consisteixen a moure qualsevol pedra pròpia a una casella buida.

Jugarem amb **taulers de 3x3** i amb **4 pedres per jugador**; però, recomanem que es pensi tot el desenvolupament de manera tal que sigui fàcil canviar la grandària del tauler i/o la quantitat de pedres per jugador. Com a orientació per assolir això, es proporcionarà un arxiu Python amb declaracions de constants i es mostrarà com es pot fer servir.

Penseu que el joc es fa interessant, per a un tauler NxN, si cada jugador té `(N^2-1)/2` pedres (sempre que `N^2-1` sigui parell).

Observem que, amb **8 pedres i 9 caselles**, a la segona fase del joc només queda una casella buida i, per tant, la jugada es pot limitar a triar quina pedra pròpia es vol moure a aquesta casella.

---

## Organització del programa

El programa que es demana constarà d'un mínim de **dos arxius Python**:
- La implementació del "tauler abstracte".
- Un o més programes "conductors" (drivers) que el facin servir per ajudar a dos jugadors humans a jugar.

S'hi poden afegir arxius addicionals si calen.

Per tal d'orientar a la tasca de programació, es proporcionaran **dos programes conductors** ja fets. Combinats amb el nostre propi "tauler abstracte" (que no proporcionarem), mostrarem a classe com fer-los servir per jugar:
- Un d'ells farà la interacció amb l'usuari humà mitjançant text.
- L'altre ho farà amb gràfics basats en **Pygame**.

Del "tauler abstracte", només estarà disponible un programa incomplet (fitxer `abs_board_h.py`), que indicarà les capçaleres de les funcions que els programes conductors poden fer servir.

L'entrega final haurà d'incloure:
- La implementació completa del tauler abstracte feta per cada equip (`abs_board.py`), que serà la base per la qualificació.
- Un o més drivers, que hauran de funcionar correctament amb el tauler abstracte programat. Poden ser els drivers proporcionats inicialment, possiblement modificats.
- Un petit informe indicant:
  - Els objectius assolits.
  - Les dificultats principals (superades o no).
  - La valoració de l'aprenentatge adquirit en fer la pràctica.
  - El repartiment de responsabilitats entre els membres de l'equip, fins al nivell de la programació de cada funció (qui ha fet què).

---

## Variants

El joc admet diverses variants interessants. Els "drivers" proporcionats actualment no n'imposen cap, només aporten el tauler, i queda a la decisió dels jugadors humans el decidir la variant. (Per exemple, aquests programes no indiquen explícitament un guanyador).

### Variants suggerides:
1. **El joc estàndar:** el primer a fer tres en ratlla guanya.
2. **La contrària:** del tipus que en anglès s'anomena freqüentment "misery" ([misère](https://en.wikipedia.org/wiki/Mis%C3%A8re), segon paràgraf): el primer jugador que fa tres en ratlla perd. Amb 4 pedres per jugador, aquesta variant es torna força interessant.

Podeu fer més variants, si ho creieu oportú, però considerant el temps que teniu i el valor final que la pràctica té dins la qualificació de PA1, pensem que és més que suficient amb la consideració d'aquestes variants.

Totes les decisions que cada equip prengui a aquest respecte hauran de venir documentades a l'informe que formi part de l'entrega.

---

## Equips

Per tal de valorar la competència transversal anomenada treball en equip, cal realitzar aquesta pràctica en **equips de dos persones**.
