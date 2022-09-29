
## Simulate Pydantic using Exception groups
As I studied Python 3.11's late features, I came across the following Exception Groups and except* features proposed in PEP-0654 see  https://peps.python.org/pep-0654/
While it was originally designed to support some libraries and recover from coroutine exceptions, its new features - running more otherwise irrelevant exceptions in one try-except clause - might prove useful in other ways as well. I developed a new BL validation pattern that allows object properties to be validated more flexible. Here is a summary:
- Verifies attributes of any object
- Run custom exception handlers for each property
- Define common exception handlers for all checked properties
- Each exception handler is defined according to its type
- Easy extension support
- Data validation should be more conscious than Pydantic, which sometimes involves some magic requiring a learning curve.
- There is no magic to this pattern; it is just a simple protocol described on one page in PEP 654.

