/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AccountsIdQuestions = function () {
    /*
        @params obj 'data params'
            id   'integer' account id in path
            content   'ref' 
            is_public   'boolean' 
            images   'array' 
            
        @success
            status 201    type:object
            listenings_count   'integer' 
            respondent   'ref' 
            images_count   'integer' 
            is_all_free   'boolean' 
            visitor_count   'ref' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/accounts/" + obj.id + "/questions",
            method: "POST",
            data: {
                content: obj.content,
                is_public: obj.is_public,
                images: obj.images
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
    AccountsIdQuestions: new AccountsIdQuestions
};