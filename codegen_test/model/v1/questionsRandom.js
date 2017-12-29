/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsRandom = function () {
    /*
        @params obj 'data params'
            question_id   'string' question id in query
            respondent_id   'integer' 
            library_id   'string' question library id in query
            
        @success
            status 200    type:object
            status   'ref' 
            free_type   'string' 
            listenings_count   'integer' 
            is_free_in_30mins   'boolean' 
            respondent   'ref' 
            account_id   'integer' 
            offer   'integer' 
            date_updated   'ref' 
            respondent_id   'ref' 
            is_free   'boolean' 
            content   'string' 
            remaining_seconds   'integer' 
            asker   'ref' 
            answer   'ref' 
            date_created   'ref' 
            type   'ref' 
            id   'string' 
            visitor_count   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/questions/random",
            method: "GET",
            data: {
                question_id: obj.question_id,
                respondent_id: obj.respondent_id,
                library_id: obj.library_id
                },
            success: function (res) {
                typeof obj.success === 'function' && obj.success(res);
            },
            fail: function (res) {
                typeof obj.fail === 'function' && obj.fail(res);
            },
            complete: function (res) {
                typeof obj.complete === 'function' && obj.complete(res);
            }
        })
    };
    

};

module.exports = {
    QuestionsRandom: new QuestionsRandom
};