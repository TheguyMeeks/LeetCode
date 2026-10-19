import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isValid(String s) {
        Deque<String> stack = new ArrayDeque<>();
        HashMap<String, String> pairs = new HashMap<>();

        pairs.put("}", "{");
        pairs.put(")", "(");
        pairs.put("]", "[");

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            String b = String.valueOf(c);
            if (pairs.containsKey(b)) {
                String top = stack.peek();
                String value = pairs.get(b);
                if (stack.isEmpty() || (!top.equals(value))) {
                    return false;
                }
                stack.pop();
            } else {
                stack.push(b);
            }
        }

        return stack.size() == 0;
    }

}