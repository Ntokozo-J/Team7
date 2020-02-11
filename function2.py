def dictionary_of_metrics(items):
    import numpy as np
    items = np.array(items)
    
    h = {'mean': round(np.mean(items)),'median': round(np.median(items)), 'variance': round(np.var(items)), 'min': round(np.min(items)), 'max': round(np.max(items)), 'standard deviation': round(np.std(items)), 'q1': round(np.quantile(items,0.25)), 'q3': round(np.quantile(items,0.75))}
    
    return h
    
    pass
    


