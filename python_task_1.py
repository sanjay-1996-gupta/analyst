import pandas as pd
df = pd.read_csv(r'C:\Users\sanja\Downloads\dataset-1.csv')

def generate_car_matrix(df):
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car')
    
    # Fill NaN values with 0, as specified
    car_matrix = car_matrix.fillna(0)
    
    # Set the diagonal values to 0
    car_matrix.values[[range(len(car_matrix))]*2] = 0
  
    print(car_matrix)
    return car_matrix
    result_matrix = generate_car_matrix(df)
    return df  
    


def get_type_count(df)->dict:
    import numpy as np
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    conditions = [(df['car'] <= 15), ((df['car']> 15) & (df['car'] <= 25)),(df['car'] > 25)]
    labels=['low', 'medium', 'high']
    df['car_type'] = np.select(conditions, labels)
    type_counts = df['car_type'].value_counts().to_dict()

    type_counts = dict(sorted(type_counts.items()))

    return type_counts

    result2 = get_type_count(df)
    print(result2)
    

                
    return dict()


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    bus_mean = df['bus'].mean()

    indices = df[df['bus'] > 2 * bus_mean].index.tolist()

    indices.sort()

    return indices


    result_indices = get_bus_indexes(df)
   
    print("Indices where bus values are greater than twice the mean:", result_indices)
    
    return list()
    
    

def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    route_avg_truck = df.groupby('route')['truck'].mean()

    # Filter routes where the average truck value is greater than 7
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

    # Sort the selected routes
    selected_routes.sort()

    return selected_routes


    result = filter_routes(df)
    print(result)
    return list()


def multiply_matrix(matrix1)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
"""

   
    matrix1 = result_matrix.copy()

    # Apply the specified logic to each value in the DataFrame
    for column in matrix1.columns:
        matrix1[column] = matrix1[column].apply(lambda x: round(x * 0.75, 1)if x > 20 else round(x * 1.25, 1))
    return matrix1       
    matrix = multiply_matrix(matrix1)
    
    print(matrix)   
    return matrix



def time_check(df2)->pd.Series:
    df2 = pd.read_csv(r'C:\Users\sanja\Downloads\dataset-2.csv')
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
    df2['startTime'] = df2['startTime'].replace('', '00:00:00')
    df2 = df2.dropna(subset=['startTime', 'endTime'])
    df2['start_datetime'] = pd.to_datetime(df2['startDay'] + ' ' + df2['startTime'], errors='coerce')
    df2['end_datetime'] = pd.to_datetime(df2['endDay'] + ' ' + df2['endTime'], errors='coerce')
    # Check if each pair covers a full 24-hour period and spans all 7 days
    completeness_check = df2.groupby(['id', 'id_2']).apply(lambda x: x['start_datetime'].min() == pd.Timestamp('00:00:00') and
                                                            x['end_datetime'].max() == pd.Timestamp('23:59:59') and
                                                            set(x['start_datetime'].dt.day_name()) == set(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
                                                           )

    return completeness_check
    return pd.Series()
    result = time_check(df2)
    print(result)

