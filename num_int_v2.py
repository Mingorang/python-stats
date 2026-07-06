# Merged with num_int when this part is done, not to be run independently.
need_for_limit = bool(input("Will you need a limit (True if the input function will approach infinity )"))
        if need_for_limit == True:
                ignore_limit = float(input("What cutoff value should be used for"))
                #Input code for this:
        elif need_for_limit == False:
                #No limit needed, run as usual
                ignore_limit = None


        #Getting IQR for ignore limit
        finite_values = f(x)[np.isfinite(f(x))]
        Q1,Q3 = np.percentile(finite_values,25), np.percentiles(finite_values, 75)
        IQR = Q3-Q1
        alpha=95
        multiplier = 1 /(1-(alpha/100))
        upper_fence = Q3 +(multiplier*IQR)
        lower_fence = Q1 - (multiplier*IQR)
        outlier_mask = (f(x) > upper_fence) | (f(x)<lower_fence) | ~np.isfinite(f(x))
        print(outlier_mask)
