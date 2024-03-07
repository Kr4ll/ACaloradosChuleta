static int MAXS = 500;
static int MAXC = 26;
static int []out = new int[MAXS];
static int []f = new int[MAXS];
static int [][]g = new int[MAXS][MAXC];
// Builds the String matching machine.
// arr -   array of words. The index of each keyword is important:
//         "out[state] & (1 << i)" is > 0 if we just found word[i]
//         in the text.
// Returns the number of states that the built machine has.
// States are numbered 0 up to the return value - 1, inclusive.
static int buildMatchingMachine(String arr[], int k)
{
    // Initialize all values in output function as 0.
    Arrays.fill(out, 0);
    // Initialize all values in goto function as -1.
    for(int i = 0; i < MAXS; i++)
        Arrays.fill(g[i], -1);
    // Initially, we just have the 0 state
    int states = 1;
    // Convalues for goto function, i.e., fill g[][]
    // This is same as building a Trie for arr[]
    for(int i = 0; i < k; ++i)
    {
        String word = arr[i];
        int currentState = 0;
        // Insert all characters of current
        // word in arr[]
        for(int j = 0; j < word.length(); ++j)
        {
            int ch = word.charAt(j) - 'a';
            // Allocate a new node (create a new state)
            // if a node for ch doesn't exist.
            if (g[currentState][ch] == -1)
                g[currentState][ch] = states++;
            currentState = g[currentState][ch];
        }
        // Add current word in output function
        out[currentState] |= (1 << i);
    }
    // For all characters which don't have
    // an edge from root (or state 0) in Trie,
    // add a goto edge to state 0 itself
    for(int ch = 0; ch < MAXC; ++ch)
        if (g[0][ch] == -1)
            g[0][ch] = 0;
    // Now, let's build the failure function
    // Initialize values in fail function
    Arrays.fill(f, -1);
    // Failure function is computed in
    // breadth first order
    // using a queue
    Queue<Integer> q = new LinkedList<>();
    // Iterate over every possible input
    for(int ch = 0; ch < MAXC; ++ch)
    {
        // All nodes of depth 1 have failure
        // function value as 0. For example,
        // in above diagram we move to 0
        // from states 1 and 3.
        if (g[0][ch] != 0) {
            f[g[0][ch]] = 0;
            q.add(g[0][ch]);
        }
    }
    // Now queue has states 1 and 3
    while (!q.isEmpty())
    {
        // Remove the front state from queue
        int state = q.peek();
        q.remove();
        // For the removed state, find failure 
        // function for all those characters
        // for which goto function is
        // not defined.
        for(int ch = 0; ch < MAXC; ++ch)
        {
            // If goto function is defined for 
            // character 'ch' and 'state'
            if (g[state][ch] != -1)
            {
                // Find failure state of removed state
                int failure = f[state];
                // Find the deepest node labeled by proper
                // suffix of String from root to current
                // state.
                while (g[failure][ch] == -1)
                      failure = f[failure];
                failure = g[failure][ch];
                f[g[state][ch]] = failure;
                // Merge output values
                out[g[state][ch]] |= out[failure];
                // Insert the next level node 
                // (of Trie) in Queue
                q.add(g[state][ch]);
            }
        }
    }
    return states;
}
// Returns the next state the machine will transition to using goto
// and failure functions.
// currentState - The current state of the machine. Must be between
//                0 and the number of states - 1, inclusive.
// nextInput - The next character that enters into the machine.
static int findNextState(int currentState, char nextInput)
{
    int answer = currentState;
    int ch = nextInput - 'a';
    // If goto is not defined, use 
    // failure function
    while (g[answer][ch] == -1)
        answer = f[answer];
    return g[answer][ch];
}
// This function finds all occurrences of
// all array words in text.
static void searchWords(String arr[], int k,
                        String text)
{
    // Preprocess patterns.
    // Build machine with goto, failure
    // and output functions
    buildMatchingMachine(arr, k);
    // Initialize current state
    int currentState = 0;
    // Traverse the text through the 
    // built machine to find all 
    // occurrences of words in arr[]
    for(int i = 0; i < text.length(); ++i)
    {
        currentState = findNextState(currentState,text.charAt(i));
        // If match not found, move to next state
        if (out[currentState] == 0)
             continue;
        // Match found, print all matching 
        // words of arr[]
        // using output function.
        for(int j = 0; j < k; ++j)
        {
            if ((out[currentState] & (1 << j)) > 0)
            {
                System.out.print("Word " +  arr[j] + 
                                 " appears from " + 
                                 (i - arr[j].length() + 1) +
                                 " to " +  i + "\n");
            }
        }
    }
}
