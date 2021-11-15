from functioning_system import stl_generator_12
import request_api

y=request_api.Y
stockname = request_api.nameofstock

if __name__ == "__main__":
    stl_generator_12.stl_generator(y, stockname)
    
print("Success! STL and picture of stock graph in you library, with short name")



