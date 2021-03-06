/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsIdReview = function () {
    /*
        @params obj 'data params'
            id   'string' question id in path
            review_action   'string' 
            
        @success
            status 200    type:object
            ok   'boolean' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/questions/" + obj.id + "/review",
            method: "PUT",
            data: {
                review_action: obj.review_action
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
    QuestionsIdReview: new QuestionsIdReview
};