# Project 4:  Brevet time calculator with Ajax

Create a replacement for the brevet controle time calculator at http://www.rusa.org/octime_acp.html in accordance with ACP rules described at http://www.rusa.org/octime_alg.html.

- Orignal author: Michal Young
- Author: Xin(Adam) Chen
- Contact Email: achen@uoregon.edu
- Contact Address: University of Oregon, 1585 E 13th Ave, Eugene, OR 97403

## Rules

- when #  Overall closing time limits vary for each brevet according to the distance.
- These are: (in hours and minutes, HH:MM) 13:30 for 200 KM, 20:00 for 300 KM, 27:00 for 400 KM, 40:00 for 600 KM, 75:00 for 1000 KM.
- The last control distance should be between the brevet distance and that distance plus 10% and return the open/close time according ot the time limits of distance.
- If distance is 0, close time should be at least 1hr.

## Example
- check point: 0km, open time: 00:00 close time: 01:00. 
- Distance: 200km
- check point: in the range between 200 to 220 (200 * 1.1)km, open time is always: 5:53 hrs, close time is 13:30hrs

## Test
- this project use nose package to test
