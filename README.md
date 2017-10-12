# TurnRight
A turnstile system proposal to replace the problematic outdated system that MDX University is using today. This new system will allow the creation of visualisation dashboards that will provide valuable insights for a better management of the library.

# About the problem
After analysing the data that the library collects, many errors were discovered that caused incorrect visualizations. For example a finding was that students that graduated 3 years ago, are still in the library since then. Also, multiple versions of the same persons were in the library at the same time. Of course, that could not have been the case! These problems arose because the library is not using a centralised system to store all the data produced, as well as allowing bad practises of the use of turnstiles. The library needs a new turnstile system that will precisely monitor the activity of the library and improve its management.

# Technologies
## Hardware
The simulation was constructed out of a shoebox, using the following technologies:

-Intel Edison IoT development kit

-Seed Grove starter kit plus components

Demonstration of the simulation can be found [here](https://www.youtube.com/watch?v=lkNqXZlRsuA)

![turnstile simulator](https://github.com/MariosGeorgiou/TurnRight/blob/master/images/turnstiles_replica.jpg)

## Software
The program was written in python(see turnstile.py). By using the attached components, it simulate how the proposed turnstile system should function.

## Synchronization software
A program was used to synchronize instantly the data stored in the csv file on the server with other administrator computers. Visualization dashboards on admins computers can now update in real time and present live information about the usage of the library.

## Visualization Dashboards
This visualization dashboard was created using Tableau and will give insight about the use of the library. 

Click [here](https://www.youtube.com/watch?v=XHXS1-kQKsU&t=24s) for a video demonstration
![turnstile simulator](https://github.com/MariosGeorgiou/TurnRight/blob/master/images/dashboard.png)


