/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var PartnerQuestionsId = function () {
    /*
        @params obj 'data params'
            id   'string' question id in path
            
        @success
            status 200    type:object
            free_type   'string' 
            category   'string' 
            listenings_count   'integer' 
            respondent   'ref' 
            date_updated   'ref' 
            asker   'ref' 
            is_free   'boolean' 
            content   'ref' 
            url   'string' 
            answer   'ref' 
            type   'ref' 
            id   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/partner/questions/" + obj.id + "",
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
    PartnerQuestionsId: new PartnerQuestionsId
};