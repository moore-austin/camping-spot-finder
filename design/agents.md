

You are here to guide people towards an interactive application which not only allows the greatest
freedom, but also the most simplicity. As their needs grow, they can dig into more complex features,
and the interface should let them know if these options, but the main function of the applications being
developed should be simple, with hidden complexities and implementation details, while allowing them to access these details and implementations if they so choose"

When creating a `blueprint.mermaid`, create it not for the specific feature at hand, but for the entire module as a whole. It is a 'quick glance' into the underworking system at hand. It practically shows the information as it moves through the application, focusing intently on triggers and responses, as well as keywords that describe the underlying meaning and reasoning inbetween.

### Mermaid Syntax Constraints (Strict Parsing)
When creating `blueprint.mermaid` or any other Mermaid diagram, you must adhere to the strict parsing rules of Mermaid v11+. 

**CRITICAL RULE: Always wrap edge labels in double quotes.**
If an edge label contains parentheses `()`, angle brackets `<>`, commas, or other special characters, the Mermaid parser will throw a fatal syntax error unless the string is explicitly quoted. To guarantee rendering stability, **you must wrap all edge labels in double quotes**.

* **INCORRECT (Will Crash):** `NodeA -->|Triggers function()| NodeB`
* **INCORRECT (Will Crash):** `NodeA -->|Parses <meta> tags| NodeB`
* **CORRECT (Safe):** `NodeA -->|"Triggers function()"| NodeB`
* **CORRECT (Safe):** `NodeA -->|"Parses <meta> tags"| NodeB`

Do not use unescaped special characters in node definitions or edge labels. When in doubt, wrap the descriptive text in quotes.

When creating an `interface.**` document, know that this interface will be seen by all other modules as the sole document by which the module will be used. Make this document simple yet elegant, as all else will be based upon it. It is ALL that other modules will need to see, and elegantly hides and shows the correct information. Clearly state in the documentation that the `ModuleNameInterface` is only representative of the `ModuleName` and should not be used directly, instead, tell them to use `ModuleName` with the same methods unless otherwise stated.


