+ using UnityEngine.UI -> accessing UI.
+ Create a text for Score. (Number) 
Using **PlayerPrefs**
	+ `PlayerPrefs is a class that stores Player preferences between game sessions.`
	+ `It can store string, float and integer values into the user’s platform registry.` 
	+ `New Name -> New Stored Varible.`



## // Store Player Score. Number can be an Default Value

```cs
PlayerPrefs.SetFloat
		   .SetString
		   .SetInteger

// Store Player Score. Number can be an Default Value
PlayerPrefs.SetInt("Name of variable", number);  
```

## // Store Player Score. Number can be an Default Value

```cs
PlayerPrefs.GetFloat
		   .GetString
		   .GetInteger

// Get the last Player Score. 
PlayerPrefs.SetInt("Name of variable", number);  
```


## Reset PlayerPrefs 
```cs
    public void Reset()
    {
        PlayerPrefs.DeleteAll();
        highScore.text = "0";
    }
```

