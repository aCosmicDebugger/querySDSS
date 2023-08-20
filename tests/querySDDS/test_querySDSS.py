from astroquery.sdss import SDSS
from astroquery.exceptions import RemoteServiceError
from requests.exceptions import ConnectionError
from astropy.table import Table
import numpy as np

def query_sdss_data():
    try:
        # Query SDSS database for necessary fields from the most recent release (e.g., DR17)
        query = """
        SELECT
            s.specobjid, s.ra, s.dec, s.z, s.class, p.flux_u, p.flux_g, p.flux_r, p.flux_i, p.flux_z
        FROM
            specObj s
        JOIN
            photoObjAll p ON s.bestObjID = p.objID
        WHERE
            s.z > 0 AND s.zWarning = 0
        """
        
        # Query SDSS database and retrieve data
        result = SDSS.query_sql(query)
        
        # Replace NaN values in flux columns with zeros
        flux_columns = ['flux_u', 'flux_g', 'flux_r', 'flux_i', 'flux_z']
        for column in flux_columns:
            result[column] = np.nan_to_num(result[column])
            
        return result
    except RemoteServiceError as e:
        print("Error querying SDSS:", e)
        return None
    except ConnectionError as e:
        print("Connection error:", e)
        return None

if __name__ == "__main__":
    # Query SDSS data
    sdss_data = query_sdss_data()
    
    if sdss_data is not None:
        # Print the retrieved data
        print(sdss_data)
    else:
        print("Error retrieving SDSS data.")

