
 <img  width="100%" src="images/seuss_flavor.jpg" alt="Seuss" /> 

___

<p float="center">
  <img img align="top" src="images/thing1.jpg" width="25%" />
  <img src="images/seuss_op.jpg" width="50%" />  
  <img src="images/thing2.jpg" width="22%" />
</p>

<br/>


<sub> This is an example of exact output. All formatting is done with python and is written into the code. *More in depth explanation further* [below.](#explanation) </sub>


<br/><br/><br/>

## &emsp; **A Peek Into How Markov Works**


<img align="right" width="300" src="images/simple_marc.jpg" alt="Markov Chain Simple Graph">
    

&emsp; A Markov chain or Markov process is a *theoretical model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event*. Informally, this may be thought of as, <strong>What happens next depends only on the state of affairs now.</strong>


<br clear="right"/>


<br/><br/><br/>

<p align="center">
<a href="https://www.youtube.com/embed/i3AkTO9HLXo"><img src="images/mc.jpg" alt="Markov Chains Clearly Explained! Part - 1" width="691" height="389" border="10" /></a>
</p>


<br/><br/><br/>


<img align="right" src="images/nest_ex.png" alt="Example of what the created dictionary looks like using Red Fish, Blue Fish" width=25%>

## Explanation
### **Brief break down of the nuances of my code.**





&emsp; Building the nested dictionaries necessary to iterate over each word in a text, tallying every word that follows it amd how many time almost broke my brain. Every word got its own dictionary containing the words that follow it and how many times. I then added the total count and used that to determine the weighted probability of each of the successive word. We then start the story with a random word, rerolling if its punctuation. We pull that words nested dictionary and, using the weighted probability, we rng the next word. Rinse and repeat until the story is as long as we want. Next, it runs through a recursive function designed to make sure each line (line is determined by when a period is called up) is no longer than 13 words, splitting at the middle comma, if there is one, and in the middle, if there isn't, capitalizing the first word in each and dropping the other down.



</br>
<br/><br/><br/>
<br/>
<img src="images/outputt.png" alt="Markov Scatter Graph" title="Markov Scatter Graph">

