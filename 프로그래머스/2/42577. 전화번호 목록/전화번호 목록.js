const solution = (phone_book) => !phone_book.sort().some((book, idx)=> phone_book[idx+1]?.indexOf(book) === 0);

 