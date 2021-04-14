/*
An IP address is a numerical label assigned to each device (e.g., computer, 
printer) participating in a computer network that uses the Internet Protocol 
for communication. There are two versions of the Internet protocol, and thus 
two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.
*/

function isIPv4Address(inputString) {

}

console.log(isIPv4Address("172.16.254.1")) //true
console.log(isIPv4Address("172.316.254.1")) //false
console.log(isIPv4Address(".254.255.0")) //false
console.log(isIPv4Address("0.254.255.0")) //true
console.log(isIPv4Address("00.254.255.0")) //false