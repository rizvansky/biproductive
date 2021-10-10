# SOLID principles
-   **(S)** Every application has only one role. Habit tracking application knows nothing about productivity or correlation, 
    Productivity application knows nothing about habit tracking and correlation, correlation analysis knows nothing about 
    habit app and productivity app and just operates on the data, stored in the database. 
    The only reason for the habit app to change is the user updating habits, the only reason for the productivity app to 
    change is the user, testing their productivities, the only reason for the correlation app to change is the user, 
    querying the analysis.
  
-   **(O) (L)** Our project is very flat, and there is no actual hierarchy of concepts and inheritance used =)
  
-   **(I)** In every app, where the database is used, Django models define the interface for the database fields and 
    methods. In every app, where the communication between frontend and backend is used, Django forms define the interface
    for the message structure and access methods.
  
-   **(D)** The database interface does not depend on its structure, but the structure depends on the interface. 
    Applications' implementation depends on abstraction in the architecture design.
  
# Design patterns used
-   Template method - correlation analysis is a skeleton of the algorithm, that calls other procedures. Redefining these 
    procedures will change the algorithm's behavior.
  
-   Module - every app is a module with a single goal and several highly related methods to achieve that goal.
-   ORM - operations on all databases are performed through abstract ORM classes.
