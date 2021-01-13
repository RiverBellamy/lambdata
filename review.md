Review of Tori's code
- Could use more comments, certainly a comment explaining each function.
- The randomize method randomizes the order of the rows, but keeps each row intact. The assignment said to randomize the cells, so the cells within a row shoudl get mixed up too.
- The null_count method is correct, but would probably be more efficient if it simply called sum() twice rather than using a python for loop
- Inheriting from Dataframe is creative. It could be a useful design choice. I'd probably call it something else though, as right now I would type Helper(...) to create a dataframe,
   and that is wierd to read.
- Some of my criticisms are nitpicky. Overall, this is pretty good clean code. It is readable, gets the job done, and is not overly verbose.