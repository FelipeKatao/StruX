# [StruX](google.com)  [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/facebook/react/blob/main/LICENSE)   ![Github-sponsors](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)  ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)  
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
  ```XML 
  <rule name="purchase" if="@value > 30" return="approved for purchase" />
```
When executed, StruX replaces @value with the real input and evaluates the rule dynamically.


## Vision

StruX aims to make systems self-explanatory, domain-aware, and driven by structure, connecting business meaning and technical precision.
  
