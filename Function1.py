def dictionary_of_metrics(items):
    import numpy as np
    
    items = np.array(items)
    h={'mean': round(np.mean(items),2),'median': round(np.median(items),2), 'variance': round(np.var(items),2), 'min': round(np.min(items)), 'max': round(np.max(items)),  'standard deviation': round(np.std(items)) }

    return h
    pass