import math

def quantize_signal(values,num_bits=-1,num_levels=-1):
    encoded_values = []
    quantized_values = []
    interval_indices = []
    error = []

    if num_levels == -1:
        num_levels= pow(2,num_bits)
    if num_bits == -1:
        num_bits = int(math.log(num_levels, 2))

    min_val = min(values)
    max_val = max(values)
    signal_range =  max_val - min_val
    delta= signal_range/num_levels
    half_delta = delta/2

    # print (f"min value is {min_val}")
    # print (f"half delta is {half_delta}")
    for val in values:
        i = min_val
        counter = -1

        if val == max_val:
            encoded_values.append(format(num_levels-1,f"0{num_bits}b"))
            quantized_values.append(max_val - half_delta)
            interval_indices.append(num_levels)
            error.append(max_val - half_delta - val)
            continue
        if val == min_val:
            encoded_values.append(format(0,f"0{num_bits}b"))
            interval_indices.append(1)
            quantized_values.append(min_val + half_delta)
            error.append(min_val + half_delta - val)
            continue


        while i <= max_val:
            if (i>=val):
                break
            q_val = i
            counter +=1
            i += delta
            i = round(i, 2)

        encoded_values.append(format(counter,f"0{num_bits}b"))
        interval_indices.append(counter+1)
        q_val+=half_delta
        quantized_values.append(round(q_val,2))
        error.append(q_val - val)
    
    return encoded_values , quantized_values , interval_indices , error






