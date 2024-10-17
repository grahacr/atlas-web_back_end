// class with static method which accepts request and returns status response and message
class AppController {
    static getHomepage(req, res) {
        res.status(200).send('Hello Holberton School!');
    }
}
module.exports = AppController;