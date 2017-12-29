/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var CrowdfundingQuestionsId = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            is_active   'boolean' 
            
        @success
            status 200    type:object
            is_active   'boolean' 
            operator_id   'ref' 
            question   'ref' 
            question_id   'ref' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/crowdfunding_questions/" + obj.id + "",
            method: "PUT",
            data: {
                is_active: obj.is_active
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
    
    /*
        @params obj 'data params'
            id   'string' string id in path
            
        @success
            status 204    type:object
            ok   'boolean' 
            
    */
    this.delete = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/crowdfunding_questions/" + obj.id + "",
            method: "DELETE",
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
    CrowdfundingQuestionsId: new CrowdfundingQuestionsId
};