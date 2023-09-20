import pandas as pd

def acceptance_rate(friend_request: pd.DataFrame, request_accepted: pd.DataFrame) -> pd.DataFrame:
    f = friend_request.drop_duplicates(['sender_id', 'send_to_id']).shape[0]
    a = request_accepted.drop_duplicates(['requester_id', 'accepter_id']).shape[0]
    rate=0 if f==0 else a/f
    return pd.DataFrame({'accept_rate': [rate]}).round(2)