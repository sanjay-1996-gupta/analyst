import pandas as pd
df1 = pd.read_csv(r'C:\Users\sanja\Downloads\dataset-3.csv') 
def calculate_distance_matrix(df1):
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame): Input dataframe containing the distances between toll locations.

    Returns:
        pandas.DataFrame: Distance matrix
    """
    # Write your logic here
    unique_ids = df1['id_start'].unique()
    distance_matrix = pd.DataFrame(index=unique_ids, columns=unique_ids).fillna(0)

    # Iterate over rows and fill in the distance_matrix
    for index, row in df1.iterrows():
        start_id, end_id, distance = row['id_start'], row['id_end'], row['distance']

        # Check if start_id and end_id are in the distance_matrix index
        if start_id in distance_matrix.index and end_id in distance_matrix.index:
            distance_matrix.at[start_id, end_id] += distance
            distance_matrix.at[end_id, start_id] += distance
        else:
            print(f"Skipped row with missing key: {start_id} or {end_id}")

    # Return the resulting distance matrix
    return distance_matrix

# Load the dataset
# df1 = pd.read_csv(r'C:\Users\sanja\Downloads\dataset-3.csv')
    
# Call the function and print the resulting distance matrix
result_distance_matrix = calculate_distance_matrix(df1)
print(result_distance_matrix)




def unroll_distance_matrix(result_distance_matrix):
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    # Write your logic here
    unrolled_data = []

    # Iterate over the rows and columns of the distance matrix
    for start_id in result_distance_matrix.index:
        for end_id in result_distance_matrix.columns:
            # Skip diagonal entries and entries with distance 0
            if start_id != end_id and result_distance_matrix.at[start_id, end_id] != 0:
                # Append the unrolled data to the list
                unrolled_data.append({'id_start': start_id, 'id_end': end_id, 'distance': result_distance_matrix.at[start_id, end_id]})

    # Create a DataFrame from the unrolled data
    unrolled_df = pd.DataFrame(unrolled_data)

    return unrolled_df

    unrolled_result_df = unroll_distance_matrix(result_distance_matrix)
    print(unrolled_result_df)


def find_ids_within_ten_percentage_threshold(unrolled_result_df, reference_id):
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Write your logic here
    reference_avg_distance = unrolled_result_df.loc[unrolled_result_df['id_start'] == reference_id, 'distance'].mean()

    # Calculate the threshold range (10% of the average distance)
    threshold = 0.1 * reference_avg_distance

    # Filter DataFrame based on the threshold range
    filtered_df = unrolled_result_df[(unrolled_result_df['id_start'] != reference_id) &
        (unrolled_result_df['distance'].between(reference_avg_distance - threshold, reference_avg_distance + threshold))  
        
        reference_id = 1001402  # Replace with the desired reference ID
        result_within_threshold = find_ids_within_ten_percentage_threshold(unrolled_result_df, reference_id)
        print(result_within_threshold)

        return filtered_df
    


def calculate_toll_rate(unrolled_result_df):
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Wrie your logic here
    moto_rate = 0.8
    car_rate = 1.2
    rv_rate = 1.5
    bus_rate = 2.2
    truck_rate = 3.6

    # Calculate toll rates for each vehicle type
    unrolled_result_df['moto'] = unrolled_result_df['distance'] * moto_rate
    unrolled_result_df['car'] = unrolled_result_df['distance'] * car_rate
    unrolled_result_df['rv'] = unrolled_result_df['distance'] * rv_rate
    unrolled_result_df['bus'] = unrolled_result_df['distance'] * bus_rate
    unrolled_result_df['truck'] = unrolled_result_df['distance'] * truck_rate
    
    result_with_toll_rates = calculate_toll_rate(unrolled_result_df)
    print(result_with_toll_rates)

    return unrolled_result_df



from datetime import datetime, time, timedelta

def calculate_time_based_toll_rates(result_within_threshold):
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        unrolled_result_df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Initialize discount factors
    weekday_discount_factors = {
        (time(0, 0, 0), time(10, 0, 0)): 0.8,
        (time(10, 0, 0), time(18, 0, 0)): 1.2,
        (time(18, 0, 0), time(23, 59, 59)): 0.8}

    weekend_discount_factor = 0.7

    # Create new columns for start_day, start_time, end_day, and end_time
    result_within_threshold['start_day'] = 'Monday'
    result_within_threshold['end_day'] = 'Sunday'
    result_within_threshold['start_time'] = time(0, 0, 0)
    result_within_threshold['end_time'] = time(23, 59, 59)

    # Apply discount factors based on time intervals
    for start_time, end_time in weekday_discount_factors.keys():
        mask = (result_within_threshold['start_time'] <= start_time) & (result_within_threshold['end_time'] >= end_time)
        result_within_threshold.loc[mask, ['start_time', 'end_time']] = start_time, end_time
        result_within_threshold.loc[mask, ['weekday_discount_factor']] = weekday_discount_factors[(start_time, end_time)]
        

    # Apply constant discount factor for weekends
    weekend_mask = (result_within_threshold['start_day'].isin(['Saturday', 'Sunday']))
    result_within_threshold.loc[weekend_mask, 'weekday_discount_factor'] = weekend_discount_factor

    # Calculate toll rates based on discount factors
    result_within_threshold['moto_rate'] = result_within_threshold['moto'] * result_within_threshold['weekday_discount_factor']
    result_within_threshold['car_rate'] = result_within_threshold['car'] * result_within_threshold['weekday_discount_factor']
    result_within_threshold['rv_rate'] = result_within_threshold['rv'] * result_within_threshold['weekday_discount_factor']
    result_within_threshold['bus_rate'] = result_within_threshold['bus'] * result_within_threshold['weekday_discount_factor']
    result_within_threshold['truck_rate'] = result_within_threshold['truck'] * result_within_threshold['weekday_discount_factor']

    return result_within_threshold


result_with_time_based_toll_rates = calculate_time_based_toll_rates(result_within_threshold)
print(result_with_time_based_toll_rates)
   
