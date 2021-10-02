# CSGO Operations Profit/Star

## Installation (e.g. with a venv)
```text
# Installation
git clone https://github.com/Mershl/csgo-operations-profit-per-star.git
cd csgo-operations-profit-per-star
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# Running
source env/bin/activate
./riptide_agents.sh
```

## Manually using script (e.g. future Missions - remember to add costs to STAR_COST_TABLE)

`overview.py https://csgostash.com/agents/Operation+Riptide+Agents`

## Supported Operations

Riptide (https://csgostash.com/agents/Operation+Riptide+Agents)

## Example output

```text
Name                                              Quality                Price
------------------------------------------------  -------------------  -------
Vypa Sista of the Revolution | Guerrilla Warfare  Master Agent           13.13
'Medium Rare' Crasswater | Guerrilla Warfare      Master Agent           13.02
Chef d'Escadron Rouchard | Gendarmerie Nationale  Master Agent           12.73
Cmdr. Frank 'Wet Sox' Baroud | SEAL Frogman       Master Agent           10.97
Cmdr. Davida 'Goggles' Fernandez | SEAL Frogman   Master Agent            7.79
Crasswater The Forgotten | Guerrilla Warfare      Master Agent            5.42
Elite Trapper Solman | Guerrilla Warfare          Superior Agent          5.9
Chem-Haz Capitaine | Gendarmerie Nationale        Superior Agent          4.59
Bloody Darryl The Strapped | The Professionals    Superior Agent          4.51
Lieutenant Rex Krikey | SEAL Frogman              Superior Agent          2.12
Arno The Overgrown | Guerrilla Warfare            Superior Agent          2.1
Col. Mangos Dabisi | Guerrilla Warfare            Exceptional Agent       4.58
Officer Jacques Beltram | Gendarmerie Nationale   Exceptional Agent       3.42
Trapper | Guerrilla Warfare                       Exceptional Agent       2.19
Lieutenant 'Tree Hugger' Farlow | SWAT            Exceptional Agent       1.48
Sous-Lieutenant Medic | Gendarmerie Nationale     Exceptional Agent       0.95
Primeiro Tenente | Brazilian 1st Battalion        Distinguished Agent     3.52
D Squadron Officer | NZSAS                        Distinguished Agent     1.33
Trapper Aggressor | Guerrilla Warfare             Distinguished Agent     1.3
Jungle Rebel | Elite Crew                         Distinguished Agent     0.83
Aspirant | Gendarmerie Nationale                  Distinguished Agent     0.71

Quality                Price Sum    ItemCount    Avg Price    Star cost    Avg Profit/Star
-------------------  -----------  -----------  -----------  -----------  -----------------
Master Agent               63.06            6       10.51            25           0.4204
Superior Agent             19.22            5        3.844           10           0.3844
Exceptional Agent          12.62            5        2.524            7           0.360571
Distinguished Agent         7.69            5        1.538            5           0.3076

Data grabbed at 2021-10-01 00:48 from https://csgostash.com/agents/Operation+Riptide+Agents
```
