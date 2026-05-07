Why never dump everything into the index. Remove duplicates and filter out low-value text, such as headers, navigation menus, or disclaimers ? 
-> Remove the Structure Noise but Keep the Semantic Headers. 
- **Examples:** "Page 5 of 10," "Confidential - Internal Use Only," "Back to Top," or website navigation menus like "Home | Products | About Us."
    
- **Why delete?** These strings appear on every page. If you embed "Page 5 of 10," that vector will be very close to the vector for "Page 6 of 10." This creates "irrelevant matches" because the retriever might think a page number is semantically related to the user's query.
    
- **Action:** **Remove completely** from the index. Do not even put them in metadata unless you have a very specific need to track document versions/confidentiality levels.
