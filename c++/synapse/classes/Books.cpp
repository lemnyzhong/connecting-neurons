#include "Books.hpp"
#include <string>

myBooks::myBooks() {}

myBooks::myBooks(std::string title, std::string author, int year) {
    author_ = author;
    bookYear_ = year;
    title_ = title;
}

const std::string myBooks::getTitle() const {
    return title_;
}

const std::string myBooks::getAuthor() const {
    return author_;
}

const int myBooks::getYear() const {
    return bookYear_;
}
