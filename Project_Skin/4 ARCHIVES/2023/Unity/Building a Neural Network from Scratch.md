

**weight** contain = biasesArray and nodeArray

![[Pasted image 20230731214859.png]]

Awake - active when an Obj was Created


![[Pasted image 20230801141756.png]]


[0,0] 0 connected to 0
[0,1] 0 connected to 0
![[Pasted image 20230801141939.png]]

![[Pasted image 20230801144629.png]]


**Guide for Evolution**
![[Pasted image 20230801160631.png]]

The Children don't learn when they Alive. They learn when they born.

```cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using static UnityEditor.Experimental.GraphView.GraphView;

public class NeuralNetworkScript : MonoBehaviour
{
    // With array we can have as many layers as wanted
    // STORE ALL LAYERS in an layers ARRAY
    public Layer[] layers;
    // network values store in here (networkShape
    public int[] networkShape = {2,4,4,2,11,7,5,9};
  
    public Layer hidden1;
    public Layer hidden2;
    public Layer output;

    public class Layer
    {
        public float[,] weightArray;
        public float[] biasesArray;
        public float[] nodesArray;

        private int n_nodes;
        private int n_inputs;

        public Layer(int n_inputs, int n_nodes)
        {
            this.n_inputs = n_inputs;
            this.n_nodes = n_nodes;

            weightArray = new float[n_nodes, n_inputs];
            biasesArray = new float[n_nodes];
            nodesArray = new float[n_nodes];
        }

		// Dùng loop để kết nối từng node với nhau,
        // connected Forward Node to Nodes
        public void Forward(float[] inputArray)
        {
            // create a new node array each time this func is called
            nodesArray = new float[n_nodes];

            for (int i = 0; i < n_nodes; i++)
            {
                // sum of weight times inputs
                for (int j = 0; j < n_inputs; j++)
                {
                    nodesArray[i] += weightArray[i, j] * inputArray[j];
                }

                // add the bias
                nodesArray[i] += biasesArray[i];
            }
        }

        // RELU
        public void Activation()
        {
            for (int i = 0; i < n_nodes; i++)
            {
                if (nodesArray[i] < 0)
                {
                    nodesArray[i] = 0;
                }
            }
        }
    }

    public void Awake()
    {
        layers = new Layer[networkShape.Length - 1];

        for (int i = 0; i < layers.Length; i++)
        {
            // Take 2 adjacent int as value in networkShape
            layers[i] = new Layer(networkShape[i], networkShape[i + 1]);
        }

        // For Loop above replace all of this
        //hidden1 = new Layer(2, 4);
        //hidden2 = new Layer(4, 4);
        //output = new Layer(4, 2);
    }
		
    // the whole Neural Network will be in this function
    public float[] Brain(float[] inputs)
    {
        hidden1.Forward(inputs);
        hidden1.Activation();
        hidden2.Forward(hidden1.nodesArray);
        hidden2.Activation();
        output.Forward(hidden2.nodesArray);

        // 3 different case that can happened
        // 1st Case: Layer get input directly from outside the network
        // 2nd Case: A hidden layer connected to another hidden layer. (most Often)
        // 3rd Case: Output Layer, don't want Activation() func

        // Each Nodes conencted to all Nodes in other Layers
        for (int i = 0; i < layers.Length; i++)
        {

            // First Layer
            if (i == 0)
            {
                layers[i].Forward(inputs);
                layers[i].Activation();
            }
             // Last Layer
            else if(i == layers.Length - 1)
            {
                layers[i].Forward(layers[i-1].nodesArray);
            }
             // Hidden Layer
            else
            {
                layers[i].Forward(layers[i - 1].nodesArray);
                layers[i].Activation();
            }
        }

        // return the last layer in our layer array
        return (layers[layers.Length - 1].nodesArray);
    }
}
```