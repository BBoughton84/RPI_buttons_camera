
import java.io.File;
import java.util.HashMap;
import java.util.Map;

import com.cloudinary.Cloudinary;
import com.cloudinary.utils.ObjectUtils;



public static void main(String arg[]){
	 
	Map config = new HashMap();
	config.put("cloud_name", "enviropi");
	config.put("api_key", "183424931379914");
	config.put("api_secret", "3GFjxQJ1ExuMU8-acIQD9yUu2MY");
	
	
	Cloudinary cloudinary = new Cloudinary(config);
	
	File file = new File()
	cloudinary.uploader().upload("test_send_pic.jpg", Object.emptyMap());
}