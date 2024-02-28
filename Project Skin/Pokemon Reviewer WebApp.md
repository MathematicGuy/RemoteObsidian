Data Base 
![[Pasted image 20240227204906.png]]

1-1 Relationship
```cs
public class Review
{
  public int Id { get; set; }
  public string Title { get; set; }
  public string Text { get; set; }
  // 1-1
  public Reviewer Reviewer { get; set; }
  // 1-1
  public Pokemon Pokemon { get; set; }


}
```
M-1 Relationship
```cs
public class Reviewer
{
  public int Id { get; set; }
  public string firstName { get; set; }
  public string lastName { get; set; }
  // M-1: Many Reviews to 1 Reviewer
  public ICollection<Review> Reviews { get; set; }
}
```
M-M (always have a JOIN)
(Require some magic (blackbox). But careful too many magic is not good)
