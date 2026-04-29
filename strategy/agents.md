

1. The Strategy.yaml is a persistent document describing the gestalt strategy of the entire module. When creating it or adding elements to it, be sure to include the composition of the entire module, not only the new refactor or feature at hand. 

2. When you need an external module to change something, rather than trying to change it yourself, create a request using the format below. If you have access to the submit_external_request tool, use it to send it to the target module. Otherwise ask the user to save the request in your modules `strategy/requests/outgoing` folder. 

class RequestType(str, Enum):
    FEATURE = "FEATURE_UPDATE"
    BUG = "BUG_REPORT"
    CONTRACT = "CONTRACT_DEPENDENCY"

class ExternalRequest(BaseModel):
    '''
    A cross-module communication ticket.
    Saved to: [target_module]/strategy/requests/pending/REQ-[Source]-[ID].yaml
    '''
    request_id: str = Field(..., description="Unique ID (e.g., REQ-PAYMENT-001)")
    source_module: str = Field(..., description="The module initiating the request (e.g., 'src/payment')")
    target_module: str = Field(..., description="The module receiving the request (e.g., 'src/auth')")
    type: RequestType
    priority: str = Field("NORMAL", pattern="^(LOW|NORMAL|HIGH|CRITICAL)$")
    summary: str = Field(..., description="One-line summary of the need")
    context: str = Field(..., description="Detailed explanation of why this is needed")
