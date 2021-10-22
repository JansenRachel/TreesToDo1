class Node {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}
class BST {
    constructor() {
        this.root = null;
    }


    // ADD
    add(val) {
        if(this.root) {
            var runner = this.root;
            while(runner) {
                if(val>runner.value) {
                    if(runner.right){
                        runner = runner.right;
                    } else {
                        runner.right = new Node(val);
                        return this
                    }
                } else {
                    if(runner.left){
                        runner = runner.left;
                    } else {
                        runner.left = new Node(val);
                        return this
                    }
                }
            }
        }
        this.root = new Node(val);
        return this
    }
    contains(val) {
        var runner = this.root;
        while (runner) {
            if (val== runner.val) {
                return true;
            }
            if (val < runner.val) {
                if (!runner.left) {
                    return false;
                }
                runner = runner.left;
            } else {
                if (!runner.right) {
                    return false;
                }
                runner = runner.right;
            }
        }
        return false;
    }
    min() {
        var runner = this.root;
        var min = this.root.val;
        while(runner.left) {
            if(runner.left.val < min) {
                min = runner.left.val;
            }
            runner = runner.left;
        }
        return min
    }
    max() {
        var runner = this.root;
        var max = this.root.val;
        while(runner.right) {
            if(runner.right.val > max) {
                max = runner.right.val;
            }
            runner = runner.right;
        }
        return max
    }
}
// creating a new BST
tree = new BST();

// add
tree.add(2).add(4).add(5).add(7).add(3).add(12).add(19).add(17).add(6).add(4)

// contains
console.log(tree.contains(17))
console.log(tree.contains('hello'))

// min
console.log(tree.min())
//max
console.log(tree.max())

console.log(tree);