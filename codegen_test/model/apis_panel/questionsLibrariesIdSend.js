/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsLibrariesIdSend = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            is_public   'boolean' 
            account_ids   'array' 
            
        @success
            status 201    type:object
            ok   'boolean' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/questions/libraries/" + obj.id + "/send",
            method: "POST",
            data: {
                is_public: obj.is_public,
                account_ids: obj.account_ids
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
    QuestionsLibrariesIdSend: new QuestionsLibrariesIdSend
};