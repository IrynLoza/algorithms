/*
With Jet Smart Cart the more items you buy, the more you save. The algorithm 
behind how this works is a bit complicated, and since it's your first day at 
Jet you decide to ask one of your co-workers for more information. In return, 
you offer to implement a new cart update algorithm for them. The update algorithm 
works like this:

Whenever a new customer visits jet.com, their shopping cart is initially empty. 
Once the customer starts shopping, the cart can receive any of the following requests:

add : <item_name>: the <item_name> item was added to the cart;
remove : <item_name>: all <item_name> items were removed from the cart;
quantity_upd : <item_name> : <value>: the <item_name> quantity in the cart was 
changed by <value>, which is an integer in the format +a or -a;
checkout: the customer has paid and the cart is now empty.

Given a list of requests in the formats described above, return the state of the cart after they have been processed. Elements in the cart should be returned in the order they were received.

Example

For

requests = ["add : milk",
            "add : pickles",
            "remove : milk",
            "add : milk",
            "quantity_upd : pickles : +4"]
the output should be
shoppingCart(requests) = ["pickles : 5", "milk : 1"];
*/

function shoppingCart(requests) {
    let cart = [];
    let hashMap = {};
    for (let i = 0; i < requests.length; i++) {
        let temp = requests[i].split(' : ');
        let index = 0;
        if (temp.includes('add')) {
             if (!(temp[1] in hashMap)) {
                hashMap[temp[1]] = 1;
            } else {
                hashMap[temp[1]]+= 1;
            }
            if (!(cart.includes(temp[1]))) {
                cart.push(`${temp[1]} : ${hashMap[temp[1]]}`)
                index = cart.includes(temp[1])
            } else {
                cart[index] = `${temp[1]} : ${hashMap[temp[1]]}`
            }
        } 
        if (temp.includes('remove')) {
            hashMap[temp[1]]-= 1;
            if (hashMap[temp[1]] <= 0) {
                cart.splice(index, 1)
            } else {
                cart[index] = `${temp[1]} : ${hashMap[temp[1]]}`
            }
        } 
        if (temp.includes('quantity_upd')) {
            let quantity = +temp[2];
            hashMap[temp[1]]+= quantity;
            cart[index] = `${temp[1]} : ${hashMap[temp[1]]}` 
        } 
        if (temp.includes('checkout')) {
            cart = [];
            hashMap = {};
        } 
        
    }
    return cart
}

console.log(shoppingCart(["add : milk",
                        "add : pickles",
                        "remove : milk",
                        "add : milk",
                        "quantity_upd : pickles : +4"])); 
                        //["pickles : 5", "milk : 1"]
console.log(shoppingCart(["add : rock",
                        "add : paper",
                        "add : scissors",
                        "checkout",
                        "add : golden medal"]));   
                        //["golden medal : 1"]                     