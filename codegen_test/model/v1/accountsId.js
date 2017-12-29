/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AccountsId = function () {
    /*
        @params obj 'data params'
            id   'integer' account id in path
            
        @success
            status 200    type:object
            listenings_count   'integer' 
            is_black   'boolean' 
            tags   'array' 
            introduction   'ref' 
            price   'integer' 
            income   'integer' 
            gravity   'integer' 
            questions_count   'integer' 
            is_receive_inquiry   'boolean' 
            recourse_replies_count   'integer' 
            is_answer_free_in_30mins   'boolean' 
            is_receive_image_question   'boolean' 
            tenant   'ref' 
            settings   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/accounts/" + obj.id + "",
            method: "GET",
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
    AccountsId: new AccountsId
};