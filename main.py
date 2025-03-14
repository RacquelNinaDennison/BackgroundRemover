from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from PIL import Image
import io
import rembg

app = FastAPI()

@app.post("/remove_bg")
async def remove_background(file: UploadFile = File(...)):
    # Read the uploaded image
    image_bytes = await file.read()
    
    # Convert bytes to a numpy array
    input_image = Image.open(io.BytesIO(image_bytes))
    
    # Process the image with Rembg
    output_image = rembg.remove(input_image)
    
    # Convert the output image to bytes
    img_byte_arr = io.BytesIO()
    output_image.save(img_byte_arr, format="PNG")  
    img_byte_arr = img_byte_arr.getvalue()
    
    # Return the processed image as HTTP response
    return Response(content=img_byte_arr, media_type="image/png")
