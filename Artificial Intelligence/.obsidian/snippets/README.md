## Simplified Guide for Customizing Obsidian Background Image 

### Default Obsidian Custom Background Image Guide (no Theme allow)
Check this guide: [How to add a custom image as a background](https://forum.obsidian.md/t/how-to-add-a-custom-image-as-a-background/53416)




### How to add a Custom Image as a Background for Everforest Enchanted Theme 
Note: Skip to step 3 if you're using a online URL. Just paste the URL and you done lol.  

Test URL: https://images.pexels.com/photos/997567/pexels-photo-997567.jpeg?w=1920&q=80


0) For faster loading speed, resize your Image to 950x520
1) Then convert your Image Type (jpg, png, etc..) to .avif (reduce file size by more than 90%)
2) Encode your Image into base64 using https://jpillora.com/base64-encoder/
3) Go to obsidian Appearance -> CSS Snipets (press folder icon) -> Create a file_name.css file inside snippets folder  
4) Paste the code the .css file then add the base64 text into the url function 
```css
:root{
  /* Background Opacity Percent*/
  --background-opacity: 0.23456; 
  /* Background Blur */
  --background-blur: 4.5678889px;
}

:root body {
  --background-image-url: url("https://images.pexels.com/photos/997567/pexels-photo-997567.jpeg?w=1920&q=80");
  
  /* Themes Background color, change variable if you change theme*/
  /* Themes Background color */
  --background-primary: rgba(var(--bg0-rgb), var(--background-opacity));
  --background-primary-alt: rgba(var(--bg0-rgb), var(--background-opacity));
  --background-secondary: rgba(var(--bg0-rgb), var(--background-opacity));
  --background-secondary-alt: rgba(var(--bg0-rgb), var(--background-opacity));
}


body::before {
  content: "";
  position: fixed; inset: 0;
  background: var(--background-image-url) center/cover no-repeat;
  filter: blur(var(--background-blur));
}
```

Check the Original Guide for more info: [custom background image guide](https://github.com/FireIsGood/obsidian-everforest-enchanted/blob/main/custom_background_image.md)
