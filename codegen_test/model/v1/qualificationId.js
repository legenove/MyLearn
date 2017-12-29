/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QualificationId = function () {
    /*
        @params obj 'data params'
            id   'string' qualification id in path
            name   'string' 
            explain   'string' 
            tag_id   'integer' 
            images   'array' 
            type   'ref' 
            additional   'string' 
            
        @success
            status 200    type:object
            status   'ref' 
            account_id   'ref' 
            title   'string' 
            reasons   'string' 
            explain   'string' 
            tag_id   'ref' 
            name   'string' 
            tag_name   'string' 
            images   'array' 
            type   'ref' 
            id   'ref' 
            additional   'string' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/qualification/" + obj.id + "",
            method: "PUT",
            data: {
                name: obj.name,
                explain: obj.explain,
                tag_id: obj.tag_id,
                images: obj.images,
                type: obj.type,
                additional: obj.additional
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
    QualificationId: new QualificationId
};