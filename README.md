# StruX
StruX is a technology focused on bridging business logic and code through the principles of Data-Oriented Programming (DOP).
It allows systems to be built around interpretable XML structures that define business rules, logic, and behaviors in a declarative and domain-driven way.

Instead of embedding rules deep inside the codebase, StruX separates them into structured data — making applications transparent, maintainable, and adaptable.

## Core Idea

``` Logic should live in data, not just in code. ```

StruX turns data into executable logic, allowing dynamic interpretation of business rules defined in XML (or other structured formats).
This creates a flexible, low-code architecture where data drives the system’s behavior.

### Key Features

* Data-Oriented Logic – behavior is defined and executed from data, not hardcoded logic.
* Business-Driven XML – rules and conditions are stored in an interpretable XML format.
* Dynamic Execution – logic can change without redeploying the backend.
* Readable by Humans and Machines – bridges business understanding and system implementation.

### Example
  ```  <rule name="purchase" if="@value > 30" return="approved for purchase" /> ```
When executed, StruX replaces @value with the real input and evaluates the rule dynamically.


## Vision

StruX aims to make systems self-explanatory, domain-aware, and driven by structure, connecting business meaning and technical precision.
  
