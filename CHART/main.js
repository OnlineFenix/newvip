
const uniqueHamburger = document.querySelector('.unique-hamburger');
const uniqueNav = document.querySelector('.unique-nav ul');
uniqueHamburger.addEventListener('click', () => {
    const isActive = uniqueHamburger.classList.toggle('active');
    uniqueNav.classList.toggle('active');
    uniqueNav.classList.toggle('inactive'); // Use inactive class to handle smooth transitions
    uniqueHamburger.setAttribute('aria-expanded', isActive);
});
const numberList = document.getElementById('numberList');
const inputField = document.getElementById('inputField');
const inputField2 = document.getElementById('inputField2');
const submitButton = document.getElementById('submitButton');
const submitButton2 = document.getElementById('submitButton2');
const keywords = ['000', '111', '222', '333', '444', '555', '666', '777', '888', '999', '0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999', 'a000', 'a111', 'a222', 'a333', 'a444', 'a555', 'a666', 'a777', 'a888', 'a999', 'b000', 'b111', 'b222', 'b333', 'b444', 'b555', 'b666', 'b777', 'b888', 'b999', '000a', '111a', '222a', '333a', '444a', '555a', '666a', '777a', '888a', '999a', '000b', '111b', '222b', '333b', '444b', '555b', '666b', '777b', '888b', '999b', 'A000', 'A111', 'A222', 'A333', 'A444', 'A555', 'A666', 'A777', 'A888', 'A999', 'B000', 'B111', 'B222', 'B333', 'B444', 'B555', 'B666', 'B777', 'B888', 'B999', '000A', '111A', '222A', '333A', '444A', '555A', '666A', '777A', '888A', '999A', '000B', '111B', '222B', '333B', '444B', '555B', '666B', '777B', '888B', '999B', '0ab', '1ab', '2ab', '3ab', '4ab', '5ab', '6ab', '7ab', '8ab', '9ab', '0ba', '1ba', '2ba', '3ba', '4ba', '5ba', '6ba', '7ba', '8ba', '9ba', '000ab', '111ab', '222ab', '333ab', '444ab', '555ab', '666ab', '777ab', '888ab', '999ab', '000ba', '111ba', '222ba', '333ba', '444ba', '555ba', '666ba', '777ba', '888ba', '999ba', '000AB', '111AB', '222AB', '333AB', '444AB', '555AB', '666AB', '777AB', '888AB', '999AB', '000BA', '111BA', '222BA', '333BA', '444BA', '555BA', '666BA', '777BA', '888BA', '999BA', 'AB000', 'AB111', 'AB222', 'AB333', 'AB444', 'AB555', 'AB666', 'AB777', 'AB888', 'AB999', 'BA000', 'BA111', 'BA222', 'BA333', 'BA444', 'BA555', 'BA666', 'BA777', 'BA888', 'BA999']

const values = Array(100).fill(0);

// Populate the list with numbers from 0 to 99
for (let i = 0; i < 100; i++) {
    const li = document.createElement('li');
    let value = values[i]
    if (i < 10) {
        i = `0${i}`
    }
    li.innerHTML = `<span class="digits">${i}</span> ${value}`;
    numberList.appendChild(li);
}
let harupIntoList = 0;
submitButton.addEventListener('click', () => {
    const input = inputField.value;
    let elementsToRemove = ["into", "intu", "Into", "Intu", "rs", "Rs", "₹", "इंटू", "ईंटो", "Total", "ttl", "Ttl", "total"];
    for (let element of elementsToRemove) {
        let regex = new RegExp(element, 'gi');
        game = input.replace(regex, '');
    }

    let lines = game.split('\n');
    let newList = [];
    lines.forEach(item => {
        const hasKeyword = keywords.some(keyword => item.includes(keyword));
        if (hasKeyword) {
            newList.push(item);
        }
    });




    lines = lines.filter(item => !newList.includes(item));

    function removeAlphabets(str) {
        let result = '';
        for (let char of str) {
            if (!/[a-zA-Z]/.test(char)) {
                result += char;
            }
        }
        return result;
    }

    function removeDuplicateSigns(str) {
        return str.replace(/([^\w])\1+/g, '$1');
    }
    lines.forEach(line => {
        line = removeAlphabets(line)
        line = removeDuplicateSigns(line)

        const pairs = line.split(/[=\(]/);

        if (pairs.length === 2) {
            const numbersStr = pairs[0];
            const amount = parseInt(pairs[1], 10);

            if (!isNaN(amount)) {
                let numbers = numbersStr.split(/[+._&: ,\/-]/)
                let newNumbers = [];
                for (num of numbers) {
                    if (num == '100') {
                        num = '0';
                        newNumbers.push(num)
                    } else {
                        newNumbers.push(num)
                    }
                };
                numberFinal = newNumbers.map(num => parseInt(num, 10));

                numberFinal.forEach(num => {
                    if (!isNaN(num) && num >= 0 && num < 100) {
                        values[num] += amount;
                        numberList.children[num].innerHTML = `<span class="digits">${num}</span> <span class="updatedValue">${values[num]}</span>`;
                    }
                });
            }
        }
    });

    let lasts = [];
    newList.forEach(item => {
        lasts.push(item.split('=' || '('))
    });

    let HARUP = []
    lasts.forEach(itemLasts => {
        for (i = itemLasts.length - 1; i >= 0; i--) {
            const harupKeywords = ['a', 'b', 'A', 'B', 'ab', 'ba', 'AB', 'BA']
            const hasKeyword = harupKeywords.some(keyword => itemLasts[i].includes(keyword));
            if (hasKeyword) {
                HARUP.push(itemLasts[i])
            }
        }
    });
    const harupKeys = ['a', 'b', 'A', 'B', 'ab', 'ba', 'AB', 'BA', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    let hList = {
        '0': '',
        '1': '',
        '2': '',
        '3': '',
        '4': '',
        '5': '',
        '6': '',
        '7': '',
        '8': '',
        '9': '',
    };
    for (h of HARUP) {
        sortHarup = h.replace(/(.)\1+/g, '$1')
        sortSide = [...new Set(h.toLowerCase().match(/[a-z]/g))]
        let harupDigit = sortHarup.match(/\d/g);
        harupDigit.forEach(digit => {
            if (!hList[digit].includes(sortSide.join(''))) {
                hList[digit] += sortSide.join('')
            }
        })
    }
    for (y in hList) {
        hList[y] = hList[y].split('')
    }
    let classList = [];
    for (items in hList) {
        if (hList[items] !== null) {
            for (into of hList[items]) {
                classList.push(`${items}${into}`)
            }
        }
    }
    let intoList = []
    for (hrf of HARUP) {
        for (i = 0; i < 10; i++) {
            if (hrf.includes(i)) {
                for (harup of classList) {
                    if (harup.includes(i)) {
                        intoList.push(`${harup}:${lasts[HARUP.indexOf(hrf)][1]}`)
                    }
                }
            }
        }
    }
    for (sepr of intoList) {
        let harupInto = sepr.split(':');
        let intoo = parseInt(harupInto[1])
        let ele = document.getElementById(harupInto[0]).innerHTML;

        valueInto = parseInt(ele) + parseInt(harupInto[1])
        document.getElementById(harupInto[0]).innerHTML = valueInto;
        harupIntoList = harupIntoList + valueInto;
    }

    inputField.value = ''; // Clear the input field
});
submitButton2.addEventListener('click', () => {
    const cross = inputField2.value;
    let splitedCross = cross.split(/[=*_#@₹:(]/)
    let crossing = splitedCross[0]
    let into = splitedCross[1]
    into = parseInt(into)

    let crossing2 = parseInt(crossing)
    if (crossing2 < 100) {
        let numbers = crossing.split(/[+._&: ,\/-]/)
        numbers.forEach(num => {
            num = parseInt(num)
            values[num] += into;
            numberList.children[num].innerHTML = `<span class="digits">${num}</span>  <span class="updatedValue">${values[num]}</span>`;
        });
    } else {
        let crossJodi = []
        for (char of crossing) {
            for (char2 of crossing) {
                let cjElement = `${char}${char2}`;
                if (!crossJodi.includes(cjElement)) {
                    crossJodi.push(cjElement);
                }
            }
        }

        crossJodi.forEach(num => {
            if (!isNaN(num)) {
                num = parseInt(num)
                values[num] += into;
                numberList.children[num].innerHTML = `<span class="digits">${num}</span>  <span class="updatedValue">${values[num]}</span>`;
            }
        });
    }
    inputField2.value = '';
});


function extractNumbers(inputString) {
    let mmList = [];
    const regex = /\d+/g;
    const numbers = inputString.match(regex);
    if (numbers) {
        mmList.push(...numbers);
    } else {
        console.log("No numbers found in the string.");
    }
    return mmList;
};


function maxValues(exampleString) {
    let minInto = 99999999;
    let maxInto = 0;
    let minJodi = ''
    let maxJodi = ''
    for (let i = 0; i < exampleString.length; i++) {
        let eList = extractNumbers(exampleString[i]);
        let mainInto = parseInt(eList[1]);
        let mainJodi = parseInt(eList[0]);
        if (mainInto < minInto && mainInto != 0) {
            minInto = mainInto;
            minJodi = mainJodi;
        }
        if (mainInto > maxInto) {
            maxInto = mainInto;
            maxJodi = mainJodi;
        }
    }
    if (minInto === 99999999) {
        minInto = 0;
    }
    return [minJodi, minInto, maxJodi, maxInto];
};

document.getElementById('check').addEventListener('click', () => {
    let emptyList = []
    for (ival in numberList.children) {
        let exportValue = numberList.children[ival].innerHTML;
        emptyList.push(`'${exportValue}'`)
    }


    let valueMinMax = maxValues(emptyList)
    document.getElementById('minJodi').innerHTML = `➾ <span>${valueMinMax[0]}: </span><span class="updatedValue">${valueMinMax[1]}</span>`;
    document.getElementById('maxJodi').innerHTML = `➾ <span>${valueMinMax[2]}: </span><span class="updatedValue">${valueMinMax[3]}</span>`;

    const harupName = document.querySelectorAll('div section ul li span:first-child');
    const harupAnder = document.querySelectorAll('div section ul li span:nth-child(2)');
    const harupBahar = document.querySelectorAll('div section ul li span:nth-child(3)');

    let secList = [
        [],
        [],
        []
    ]

    harupName.forEach(item => {
        secList[0].push(item.innerHTML)
    })

    harupAnder.forEach(item => {
        secList[1].push(item.innerHTML)
    })

    harupBahar.forEach(item => {
        secList[2].push(item.innerHTML)
    })


    let harupMax = [
        [],
        [],
        []
    ]


    secList[0].forEach(item => {
        harupMax[0].push(item)
    })
    secList[1].forEach(item => {
        harupMax[1].push(item)
    })
    secList[2].forEach(item => {
        harupMax[2].push(item)
    })

    function findMax(arr) {
        let maxHarup = 0
        let nameHrf = ''
        for (item in arr) {
            if (arr[item] != 'Ander' || arr[item] != 'Bahar' || arr[item] != 0) {
                maxItem = parseInt(arr[item])
                if (maxItem > maxHarup) {
                    maxHarup = maxItem
                    nameHrf = harupMax[0][item]
                }
            }
        }
        return [nameHrf, maxHarup];
    }
    let ander = findMax(harupMax[1]);
    let bahar = findMax(harupMax[2]);

    document.getElementById('maxHarupA').innerHTML = `➾ <span>${ander[0]}: </span><span class="updatedValue">${ander[1]}</span>`;
    document.getElementById('maxHarupB').innerHTML = `➾ <span>${bahar[0]}: </span><span class="updatedValue">${bahar[1]}</span>`;

    let ttl = document.querySelectorAll('#numberList li span:nth-child(2)')
    totalAmount = 0
    ttl.forEach(e => {
        let amount = parseInt(e.innerHTML)
        totalAmount = totalAmount + amount
    })
    const finalAmount = totalAmount + harupIntoList
    document.getElementById('totalAmount').innerHTML = `➾ <span class="updatedValue">${finalAmount}</span>`;
})


// Copy button
document.getElementById('advButton-1').addEventListener('click', () => {
    let emptyListGlobal = []
    for (ival in numberList.children) {
        let exportValue = numberList.children[ival].innerHTML;
        emptyListGlobal.push(`'${exportValue}'`)
    }
    let textCopy = ["JODI____AMOUNT\n"]
    for (i in emptyListGlobal) {
        let ev = extractNumbers(emptyListGlobal[i])
        if (ev[1] != 0 && ev[1] != undefined) {
            textCopy.push(`➛ ${ev[0]} => ${ev[1]} INTO \n`)
        }
    }
    const harupName = document.querySelectorAll('div section ul li span:first-child');
    const harupAnder = document.querySelectorAll('div section ul li span:nth-child(2)');
    const harupBahar = document.querySelectorAll('div section ul li span:nth-child(3)');

    let secList = [
        [],
        [],
        []
    ]


    let testList = ["\n\nHarup——Ander——Bahar\n"]
    for (j in harupAnder) {
        let h = harupName[j].innerHTML
        let a = harupAnder[j].innerHTML
        let b = harupBahar[j].innerHTML

        if (h != undefined && h != 'Harup' && (a != 0 || b != 0)) {
            testList.push(`[[${h}]]——₹${a}——₹${b}\n`)
        }
    }

    function replaceSingleItem(list) {
        if (list.length === 1) {
            list[0] = '';
        }
        return list;
    }

    textCopy = replaceSingleItem(textCopy)
    testList = replaceSingleItem(testList)

    const finalCopy = `${textCopy.join('')}${testList.join('')}`
    if (finalCopy.length === 0) {
        alert("Please enter some data first")
    } else {
        navigator.clipboard.writeText(finalCopy)
        alert("Text Copied!")
    }
})

// Share Button

document.getElementById('advButton-2').addEventListener('click', () => {
    let emptyListGlobal = []
    for (ival in numberList.children) {
        let exportValue = numberList.children[ival].innerHTML;
        emptyListGlobal.push(`'${exportValue}'`)
    }
    let textCopy = ["JODI____AMOUNT\n"]
    for (i in emptyListGlobal) {
        let ev = extractNumbers(emptyListGlobal[i])
        if (ev[1] != 0 && ev[1] != undefined) {
            textCopy.push(`➛ ${ev[0]} => ${ev[1]} INTO \n`)
        }
    }
    const harupName = document.querySelectorAll('div section ul li span:first-child');
    const harupAnder = document.querySelectorAll('div section ul li span:nth-child(2)');
    const harupBahar = document.querySelectorAll('div section ul li span:nth-child(3)');

    let secList = [
        [],
        [],
        []
    ]


    let testList = ["\n\nHarup——Ander——Bahar\n"]
    for (j in harupAnder) {
        let h = harupName[j].innerHTML
        let a = harupAnder[j].innerHTML
        let b = harupBahar[j].innerHTML

        if (h != undefined && h != 'Harup' && (a != 0 || b != 0)) {
            testList.push(`[[${h}]]——₹${a}——₹${b}\n`)
        }
    }

    function replaceSingleItem(list) {
        if (list.length === 1) {
            list[0] = '';
        }
        return list;
    }

    textCopy = replaceSingleItem(textCopy)
    testList = replaceSingleItem(testList)

    const finalCopy = `${textCopy.join('')}${testList.join('')}`
    if (finalCopy.length === 0) {
        alert("Please enter some data first")
    } else {
        navigator.share({
            title: 'Jantri: vip-satta-result.in',
            text: finalCopy,
        })
    }
    })