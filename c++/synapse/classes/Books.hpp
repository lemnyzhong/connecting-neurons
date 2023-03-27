#ifndef BOOKS_HPP
#define BOOKS_HPP
#include <string>

class myBooks {
    private:
        std::string title_ {};
        std::string author_ {};
        int bookYear_ = 0;

    public:
        myBooks();

        myBooks(std::string title, std::string author, int year);

        const std::string getTitle() const;

        const std::string getAuthor() const;

        const int getYear() const;
};
#endif